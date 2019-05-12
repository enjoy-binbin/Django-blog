;(function (factory) {
    if (typeof define === 'function' && define.amd) {
        define(['jquery'], factory);
    } else if (typeof exports === 'object') {
        factory(require('jquery'));
    } else {
        factory(jQuery);
    }
})(function ($) {
    'use strict';
    var $W = $(window), $D = $(document), jqEle = null, isMoving = false, isResizing = false;
    var EVENTS = {
        CLICK: 'click',
        KEYDOWN: 'keydown',
        RESIZE: 'resize',
        WHEEL: 'wheel mousewheel DOMMouseScroll',
        MOUSESTART: 'mousedown',
        MOUSEMOVE: 'mousemove',
        MOUSEEND: 'mouseup',
        EVENT_NS: '.magnify'
    };
    var cssSelector = {
        'modal': '.magnify-modal',
        'header': '.magnify-header',
        'footer': '.magnify-footer',
        'toolbar': '.magnify-toolbar',
        'stage': '.magnify-stage',
        'title': '.magnify-title',
        'image': '.magnify-image',
        'close': '.magnify-btn-close',
        'zoomIn': '.magnify-btn-zoomIn',
        'zoomOut': '.magnify-btn-zoomOut',
        'prev': '.magnify-btn-prev',
        'next': '.magnify-btn-next',
        'actualSize': '.magnify-btn-actualSize',
        'rotateLeft': '.magnify-btn-rotateLeft',
        'rotateRight': '.magnify-btn-rotateRight',
        'loader': '.magnify-loader',
        'btn': '.magnify-btn',
        // 0412增加两个按钮, 删除和跳转到
        'delete': '.magnify-btn-delete',
        'jump_to': '.magnify-btn-jump_to',
    };
    var defaults = {
        draggable: false,
        resizable: false,
        movable: false,
        keyboard: false,
        title: true,
        Toolbar: ['prev', 'next', 'rotateLeft', 'rotateRight', 'zoomIn', 'actualSize', 'zoomOut'], // 0412按钮添加
        i18n: {
            close: '关闭(Esc)',
            zoomIn: '放大(+)',
            zoomOut: '缩小(-)',
            prev: '上一张(←)',
            next: '下一张(→)',
            actualSize: '实际尺寸(Ctrl + 5)',
            rotateLeft: '左旋转(Ctrl + 4)',
            rotateRight: '右旋转(Ctrl + 6)',
            delete: '删除图片(Del)',  // 按钮提示title
            jump_to: '跳转',  // 跳转按钮
        },
        modalSize: [800, 600],
        modalOffset: [0, 0],
        ratioThreshold: 0.1,
        minRatio: 0.1,
        maxRatio: 16,
        dragHandle: false,
        beforeOpen: null,
        opened: null,
        beforeClose: null,
        closed: null,
        beforeChange: null,
        changed: null,
        ieTransforms: {
            '0': 'progid:DXImageTransform.Microsoft.BasicImage(rotation=0)',
            '90': 'progid:DXImageTransform.Microsoft.BasicImage(rotation=1)',
            '180': 'progid:DXImageTransform.Microsoft.BasicImage(rotation=2)',
            '270': 'progid:DXImageTransform.Microsoft.BasicImage(rotation=3)'
        }
    };
    var magnify = function (ele, opts) {
        this.settings = $.extend(true, {}, defaults, opts);
        if (opts && $.isArray(opts.Toolbar)) {
            if (opts.Toolbar.length !== defaults.Toolbar.length) {
                this.settings.Toolbar = opts.Toolbar;
            } else {
                this.settings.Toolbar = defaults.Toolbar;
            }
        }
        this.$ele = $(ele);
        this.isOpened = false;
        this.isRotated = false;
        this.rotateAngle = 0;
        this.imageData = {};
        this.modalData = {width: null, height: null, left: null, top: null};
        this.init(ele);
    };
    magnify.prototype = {
        init: function (ele) {
            var imgSrc = getImgSrc(ele);
            this.groupName = null;
            var currentGroupName = $(ele).data('group');
            var groupList = $D.find('[data-group="' + currentGroupName + '"]');
            if (currentGroupName !== undefined) {
                this.groupName = currentGroupName;
                this.getImgGroup(groupList, imgSrc);
            } else {
                this.getImgGroup(jqEle.not('[data-group]'), imgSrc);
            }
            this.open();
            this.loadImg(imgSrc);
            if (this.settings.draggable) {
                this.draggable(this.$magnify, this.dragHandle, cssSelector.btn)
            }
            if (this.settings.movable) {
                this.movable(this.$stage, this.$image);
            }
            if (this.settings.resizable) {
                this.resizable(this.$magnify, this.$stage, this.$image, this.settings.modalSize);
            }
        }, open: function () {
            if ($(cssSelector.modal)) {
                $(cssSelector.modal).remove();
            }
            this.build();
            this.triggerHook('beforeOpen', this.$ele);
            $('body').append(this.$magnify);
            this.addEvents();
            this.setModalPos(this.$magnify);
            this.triggerHook('opened', this.$ele);

            // 0412最外面遮罩层
            $('.overlay').css({'height': $(document).height(), 'width': $(document).width()}).show();

        }, build: function () {
            var _html = this.createDOM();
            var $magnify = $(_html);
            this.$magnify = $magnify;
            this.$stage = $magnify.find(cssSelector.stage);
            this.$title = $magnify.find(cssSelector.title);
            this.$image = $magnify.find(cssSelector.image);
            this.$close = $magnify.find(cssSelector.close);
            this.$zoomIn = $magnify.find(cssSelector.zoomIn);
            this.$zoomOut = $magnify.find(cssSelector.zoomOut);
            this.$prev = $magnify.find(cssSelector.prev);
            // this.$prev2 = $magnify.find(cssSelector.prev2);0412
            this.$next = $magnify.find(cssSelector.next);
            // this.$next2 = $magnify.find(cssSelector.next2);
            this.$fullScreen = $magnify.find(cssSelector.fullScreen);
            this.$actualSize = $magnify.find(cssSelector.actualSize);
            this.$rotateLeft = $magnify.find(cssSelector.rotateLeft);
            this.$rotateRight = $magnify.find(cssSelector.rotateRight);
            if (!this.settings.dragHandle || this.settings.dragHandle === cssSelector.modal) {
                this.dragHandle = this.$magnify;
            } else {
                this.dragHandle = this.$magnify.find(this.settings.dragHandle);
            }
        }, createDOM: function () {
            var btnTpl = {
                zoomIn: '<a href="javascript:void(0)" class="magnify-btn magnify-btn-zoomIn" title="' + this.settings.i18n.zoomIn + '"></a>',
                zoomOut: '<a href="javascript:void(0)" class="magnify-btn magnify-btn-zoomOut" title="' + this.settings.i18n.zoomOut + '"></a>',
                prev: '<a href="javascript:void(0)" class="magnify-btn magnify-btn-prev" title="' + this.settings.i18n.prev + '"></a>',
                next: '<a href="javascript:void(0)" class="magnify-btn magnify-btn-next" title="' + this.settings.i18n.next + '"></a>',
                actualSize: '<a href="javascript:void(0)" class="magnify-btn magnify-btn-actualSize" title="' + this.settings.i18n.actualSize + '"></a>',
                rotateLeft: '<a href="javascript:void(0)" class="magnify-btn magnify-btn-rotateLeft" title="' + this.settings.i18n.rotateLeft + '"></a>',
                rotateRight: '<a href="javascript:void(0)" class="magnify-btn magnify-btn-rotateRight" title="' + this.settings.i18n.rotateRight + '"></a>',
                delete: '<a id="photo-delete" href="javascript:void(0)" class="magnify-btn magnify-btn-delete" title="' + this.settings.i18n.delete + '"></a>',
                jump_to: '<a href="javascript:void(0)" class="magnify-btn magnify-btn-jump_to" title="' + this.settings.i18n.jump_to + '"></a>',
            };
            return '<div class="magnify-modal">' +
                '<div class="magnify-header">' + this.createTitle() +
                '<a href="javascript:void(0)" class="magnify-btn-close" title="' + this.settings.i18n.close + '"></a>' +
                '</div>' +
                '<div class="magnify-stage">' +
                // '<div class="magnify-toolbar" style="">' + this.createPreBtn() +
                '<img src="" alt="" title="' + '" class="magnify-image" style="position: absolute;transform: rotate(0deg); transform-origin: 50% 50% 0px;">' +
                this.createNextBtn() + '</div>' +
                '<div>555555555</div>' +
                '<div class="magnify-footer"><div class="magnify-toolbar">' + this.createBtn(this.settings.Toolbar, btnTpl) + '</div></div>' +
                '</div>';
        }, createTitle: function () {
            return this.settings.title ? '<div class="magnify-title"></div>' : '';
        },

        // 0412: 增加多两个上一页下一页，整个弹出框左半部分和右半部分可点分别对应上下页
        createPreBtn: function () {
            var width = $W.width() * 0.9 * 0.5 + 'px';
            var height = $W.height() * 0.9 + 'px';
            var PreBtnStr = '<a style="width: ' + width + '; height: ' + height + ';" href="javascript:void(0)" class="magnify-btn magnify-btn-prev my-pre" title="上一张(←)"></a>';
            return '';
        },
        createNextBtn: function () {
            var width = $W.width() * 0.9 * 0.5 + 'px';
            var height = $W.height() * 0.9 - 100 + 'px';
            var NextBtnStr = '<a style="width: ' + width + '; height: ' + height + ';" href="javascript:void(0)" class="magnify-btn magnify-btn-next my-next" title="下一张(→)"></a>'
            return '';
        },
        // 0412, 完成

        createBtn: function (toolbar, btns) {
            var btnStr = '';
            $.each(toolbar, function (index, item) {
                btnStr += btns[item];
            });

            return btnStr;
        }, setModalSize: function () {
            var self = this;
            var $modal = this.$magnify;
            var winWidth = $W.width();
            var winHeight = $W.height();
            var newLeft = (winWidth - self.modalData.width) / 2;
            var newTop = (winHeight - self.modalData.height) / 2;
            $modal.css({left: newLeft, top: newTop});
            $.extend(self.modalData, {left: newLeft, top: newTop})
        }, setModalPos: function (modal) {
            var winWidth = $W.width(), winHeight = $W.height(), modalSize = this.settings.modalSize,
                modalWidth = modalSize[0], modalHeight = modalSize[1];

            // 0412: 弹出框要根据页面大小来定，接近全覆盖的大小
            modalWidth = winWidth * 0.6;
            modalHeight = winHeight * 0.95;
            // 0412, 完成, 根据 jquery的$(window).height() or $(window).width() 获取当前浏览器可视区域宽高

            modal.css({
                width: modalWidth,
                height: modalHeight,
                left: (winWidth - modalWidth) / 2,
                top: (winHeight - modalHeight) / 2
            });
            $.extend(this.modalData, {
                width: modalWidth,
                height: modalHeight,
                left: (winWidth - modalWidth) / 2,
                top: (winHeight - modalHeight) / 2
            });
            this.isOpened = true;
        }, setImageSize: function (img, tag) {
            var stageData = {w: this.$stage.width(), h: this.$stage.height()};
            var scale = 1;
            if (!this.isRotated) {
                scale = Math.min(stageData.w / img.width, stageData.h / img.height, 1);
            } else {
                scale = Math.min(stageData.w / img.height, stageData.h / img.width, 1);
            }
            if (this.isRotated && tag === 'jump') {
                this.$image.css({
                    left: (stageData.w - this.$image.width()) / 2,
                    top: (stageData.h - this.$image.height()) / 2
                })
            } else {
                this.$image.css({
                    width: Math.ceil(img.width * scale),
                    height: Math.ceil(img.height * scale),
                    left: (stageData.w - Math.ceil(img.width * scale)) / 2,
                    top: (stageData.h - Math.ceil(img.height * scale)) / 2
                });
            }
            $.extend(this.imageData, {
                width: img.width * scale,
                height: img.height * scale,
                left: (stageData.w - img.width * scale) / 2,
                top: (stageData.h - img.height * scale) / 2
            });
            setGrabCursor({w: this.$image.width(), h: this.$image.height()}, {
                w: this.$stage.width(),
                h: this.$stage.height()
            }, this.$stage, this.isRotated);
            this.$magnify.find(cssSelector.loader).remove();
            this.$image.fadeIn();
        }, loadImg: function (imgSrc, tag) {
            var self = this;
            var loadHTML = '<div class="magnify-loader"></div>';
            this.$magnify.append(loadHTML);
            self.$image.attr('src', imgSrc);
            preLoadImg(imgSrc, function (img) {
                self.imageData = {originalWidth: img.width, originalHeight: img.height};
                self.setImageSize(img, tag);
            }, function () {
                self.$magnify.find(cssSelector.loader).remove();
            });
            if (this.settings.title) {
                this.setImgTitle();
            }
        }, getImgGroup: function (list, imgSrc) {
            var self = this;
            self.groupData = [];
            $(list).each(function (index, item) {
                var src = getImgSrc(item);
                self.groupData.push({src: src, caption: $(item).data('caption')});
                if (imgSrc === src) {
                    self.groupIndex = index;
                }
            })
        }, setImgTitle: function () {
            var index = this.groupIndex;
            var caption = this.groupData[index].caption;
            caption = caption ? caption : '';
            this.$title.text(caption);
        }, triggerHook: function (e, data) {
            if (typeof this.settings[e] === 'function') {
                typeof this.settings[e].call(this, $.isArray(data) ? data : [data], this.$magnify);
            }
        }, addEvents: function () {
            var self = this;
            this.$close.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.close();
            });

            // 0416: div#overlay, 点击遮罩层外部可以关闭图片展示弹出框
            $('#overlay').off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.close();
            });
            // this.$header.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
            //     // event.preventDefault();  // 阻止默认事件
            //     event.stopPropagation();  // 阻止冒泡

            // 0416，给jump_to按钮添加事件
            this.$jump_to = this.$magnify.find(cssSelector.jump_to);
            this.$jump_to.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                alert('正在开发此功能');
            });

            this.$delete = this.$magnify.find(cssSelector.delete);
            this.$delete.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                let name = $('.magnify-title').text();
                deletePhotoImage(name);

            });

            this.$prev.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.jump(-1);
            });
            this.$next.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.jump(1);
            });
            // 0412
            // this.$prev2.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
            //     self.jump(-1);
            // });
            // this.$next2.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
            //     self.jump(1);
            // });

            this.$zoomIn.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.zoom(self.settings.ratioThreshold * 3, {x: self.$stage.width() / 2, y: self.$stage.height() / 2});
            });
            this.$zoomOut.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.zoom(-self.settings.ratioThreshold * 3, {x: self.$stage.width() / 2, y: self.$stage.height() / 2});
            });
            this.$actualSize.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.actualSize();
            });
            this.$rotateLeft.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.rotate(-90);
            });
            this.$rotateRight.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function () {
                self.rotate(90);
            });
            this.$stage.off(EVENTS.WHEEL + EVENTS.EVENT_NS).on(EVENTS.WHEEL + EVENTS.EVENT_NS, function (e) {
                self.wheel(e);
            });
            $D.off(EVENTS.KEYDOWN + EVENTS.EVENT_NS).on(EVENTS.KEYDOWN + EVENTS.EVENT_NS, function (e) {
                self.keyDown(e);
            });
            $W.on(EVENTS.RESIZE + EVENTS.EVENT_NS, function () {
                self.resize();
            });
        }, close: function () {
            this.triggerHook('beforeClose', this.$ele);
            this.$magnify.remove();
            this.isRotated = false;
            this.isOpened = false;
            this.rotateAngle = 0;
            $D.off(EVENTS.KEYDOWN + EVENTS.EVENT_NS);
            $W.off(EVENTS.RESIZE + EVENTS.EVENT_NS);
            this.triggerHook('closed', this.$ele);

            // 0412关闭最外面的遮罩层
            $('#overlay').hide();
        }, wheel: function (e) {
            stopPre(e);
            var delta = 1;
            if (e.originalEvent.deltaY) {
                delta = e.originalEvent.deltaY > 0 ? 1 : -1;
            } else if (e.originalEvent.wheelDelta) {
                delta = -e.originalEvent.wheelDelta / 120;
            } else if (e.originalEvent.detail) {
                delta = e.originalEvent.detail > 0 ? 1 : -1;
            }
            var ratio = -delta * this.settings.ratioThreshold;
            var pointer = {
                x: e.originalEvent.clientX - this.$stage.offset().left + $D.scrollLeft(),
                y: e.originalEvent.clientY - this.$stage.offset().top + $D.scrollTop()
            };
            this.zoom(ratio, pointer, e);
        }, zoom: function (ratio, origin) {
            ratio = ratio < 0 ? (1 / (1 - ratio)) : (1 + ratio);
            if (ratio > 0.95 && ratio < 1.05) {
                ratio = 1;
            }
            ratio = parseInt(this.$image[0].style.width) / this.imageData.originalWidth * ratio;
            ratio = Math.max(ratio, this.settings.minRatio);
            ratio = Math.min(ratio, this.settings.maxRatio);
            var $image = this.$image;
            var $stage = this.$stage;
            var imgData = {
                w: this.imageData.width,
                h: this.imageData.height,
                x: this.imageData.left,
                y: this.imageData.top
            };
            var stageData = {w: $stage.width(), h: $stage.height(), x: $stage.offset().left, y: $stage.offset().top};
            var newWidth = this.imageData.originalWidth * ratio;
            var newHeight = this.imageData.originalHeight * ratio;
            var newLeft = origin.x - (origin.x - imgData.x) / imgData.w * newWidth;
            var newTop = origin.y - (origin.y - imgData.y) / imgData.h * newHeight;
            var gt = !this.isRotated ? 0 : (newWidth - newHeight) / 2;
            var imgNewWidth = !this.isRotated ? newWidth : newHeight;
            var imgNewHeight = !this.isRotated ? newHeight : newWidth;
            var offsetX = stageData.w - newWidth;
            var offsetY = stageData.h - newHeight;
            $image.css({width: Math.round(newWidth), height: Math.round(newHeight)});
            var imgCurrWidth = $image.width();
            var imgCurrHeight = $image.height();
            if (imgNewWidth <= stageData.w) {
                newLeft = (stageData.w - imgCurrWidth) / 2;
            } else {
                newLeft = -(imgCurrWidth - stageData.w) / 2;
            }
            if (imgNewHeight <= stageData.h) {
                newTop = (stageData.h - imgCurrHeight) / 2;
            } else {
                newTop = -(imgCurrHeight - stageData.h) / 2;
            }
            $image.css({left: Math.round(newLeft), top: Math.round(newTop)});
            $.extend(this.imageData, {width: newWidth, height: newHeight, left: newLeft, top: newTop});
            setGrabCursor({w: Math.round(imgNewWidth), h: Math.round(imgNewHeight)}, {
                w: stageData.w,
                h: stageData.h
            }, this.$stage);
        }, jump: function (n) {
            var groupLen = this.groupData.length;
            if (n > 0) {
                if (this.groupIndex + n >= groupLen) {
                    n = 0
                } else {
                    n = this.groupIndex + 1
                }
            }
            if (n < 0) {
                if (this.groupIndex + n < 0) {
                    n = groupLen + n;
                } else {
                    n = this.groupIndex + n
                }
            }
            this.groupIndex = n;
            this.triggerHook('beforeChange', n);
            this.loadImg(this.groupData[n].src, 'jump');
            this.triggerHook('changed', n);
        }, actualSize: function () {
            this.isRotated = false;
            this.rotateAngle = 0;
            this.$image.css({transform: 'rotate(0deg)'});
            var useIeTransforms = function () {
                var isIE = false;
                if (navigator.appName === 'Microsoft Internet Explorer') {
                    if (navigator.userAgent.match(/Trident/i) && navigator.userAgent.match(/MSIE 8.0/i)) {
                        isIE = true
                    }
                }
                return isIE;
            }();
            if (useIeTransforms) {
                this.$image.css('filter', 'progid:DXImageTransform.Microsoft.BasicImage(rotation=0)');
            }
            this.loadImg(this.groupData[this.groupIndex].src);
        }, rotate: function (angle) {
            var self = this;
            this.rotateAngle = this.rotateAngle + angle;
            this.isRotated = (this.rotateAngle / 90) % 2 !== 0;
            self.transformDeg(this.$image, self.rotateAngle);
        }, transformDeg: function (currentImg, currentDeg) {
            var unit = this;
            var useIeTransforms = function () {
                var isIE = false;
                if (navigator.appName === 'Microsoft Internet Explorer') {
                    if (navigator.userAgent.match(/Trident/i) && navigator.userAgent.match(/MSIE 8.0/i)) {
                        isIE = true
                    }
                }
                return isIE;
            }();
            var cssVal = 'rotate(' + currentDeg + 'deg)';
            var _style = ['', '-webkit-', '-moz-', '-o-', '-ms-'];
            for (var i = 0; i < _style.length; i++) {
                var prefix = _style[i];
                currentImg.css(prefix + 'transform', cssVal);
            }
            if (useIeTransforms) {
                var _IeStyle = ['-ms-', ''];
                for (var j = 0; j < _IeStyle.length; j++) {
                    var IEprefix = _IeStyle[j];
                    if (Math.abs(currentDeg) >= 360) {
                        currentDeg = currentDeg % 360
                    }
                    currentImg.css(IEprefix + 'filter', unit.settings.ieTransforms[Math.abs(currentDeg)]);
                    var imgHeightNum = currentImg.height();
                    var imgWidthNum = currentImg.width();
                    if (defaults.modalSize[0] >= imgHeightNum) {
                        currentImg.css(IEprefix + 'left', defaults.modalSize[0] / 2 - imgWidthNum / 2 + 'px');
                        currentImg.css(IEprefix + 'top', defaults.modalSize[1] / 2 - imgHeightNum / 2 + 'px');
                    } else {
                        currentImg.css(IEprefix + 'left', -(imgWidthNum - defaults.modalSize[0]) / 2 + 'px')
                        currentImg.css(IEprefix + 'top', -(imgHeightNum - defaults.modalSize[1]) / 2 + 'px')
                    }
                }
            }
        }, resize: function () {
            var self = this;
            return throttle(function () {
                self.setModalSize()
            }, 500);
        }, keyDown: function (e) {
            var self = this;
            if (!this.settings.keyboard) return false;
            var keyCode = e.keyCode || e.which || e.charCode;
            var ctrlKey = e.ctrlKey || e.metaKey;
            var altKey = e.altKey || e.metaKey;
            console.log(keyCode);
            switch (keyCode) {
                // 0411: 图片显示和快捷键设置
                case 46:
                    // 删除 Del
                    break;
                case 27:  // 关闭 ESC
                    self.close();
                    break;
                case 37:  // 上一张 方向键 left
                    self.jump(-1);
                    break;
                case 39:  // 下一张 方向键 right
                    self.jump(1);
                    break;
                case 107:  // 放大  数字键 +
                    self.zoom(self.settings.ratioThreshold * 3, {
                        x: self.$stage.width() / 2,
                        y: self.$stage.height() / 2
                    });
                    break;
                case 109:  // 缩小 数字键 -
                    self.zoom(-self.settings.ratioThreshold * 3, {
                        x: self.$stage.width() / 2,
                        y: self.$stage.height() / 2
                    });
                    break;
                case 100:  // 左旋转
                    if (ctrlKey) {
                        self.rotate(-90);
                    }
                    break;
                case 102:  // 右旋转
                    if (ctrlKey) {
                        self.rotate(90);
                    }
                    break;
                case 101:  // 恢复
                    if (ctrlKey) {
                        self.actualSize();
                    }
                    break;
            }
        }, movable: function (stage, image) {
            var self = this, isDragging = false, startX = 0, startY = 0, left = 0, top = 0, widthDiff = 0,
                heightDiff = 0, gt = 0;
            var dragStart = function (e) {
                stopPre(e);
                var imgWidth = $(image).width();
                var imgHeight = $(image).height();
                var stageWidth = $(stage).width();
                var stageHeight = $(stage).height();
                startX = e.clientX;
                startY = e.clientY;
                gt = !self.isRotated ? 0 : (imgWidth - imgHeight) / 2;
                widthDiff = !self.isRotated ? imgWidth - stageWidth : imgHeight - stageWidth;
                heightDiff = !self.isRotated ? imgHeight - stageHeight : imgWidth - stageHeight;
                isDragging = widthDiff > 0 || heightDiff > 0 ? true : false;
                isMoving = widthDiff > 0 || heightDiff > 0 ? true : false;
                left = $(image).position().left - gt;
                top = $(image).position().top + gt;
                if (stage.hasClass('is-grab')) {
                    $('html,body,.magnify-modal,.magnify-stage,.magnify-btn').addClass('is-grabbing');
                }
                $D.on(EVENTS.MOUSEMOVE + EVENTS.EVENT_NS, dragMove).on(EVENTS.MOUSEEND + EVENTS.EVENT_NS, dragEnd);
            };
            var dragMove = function (e) {
                stopPre(e);
                if (isDragging) {
                    var endX = e.clientX, endY = e.clientY;
                    var relativeX = endX - startX, relativeY = endY - startY;
                    var newLeft = relativeX + left, newTop = relativeY + top;
                    if (heightDiff > 0) {
                        if (relativeY + top > gt) {
                            newTop = gt;
                        } else if (relativeY + top < -heightDiff + gt) {
                            newTop = -heightDiff + gt;
                        }
                    } else {
                        newTop = top;
                    }
                    if (widthDiff > 0) {
                        if (relativeX + left > -gt) {
                            newLeft = -gt;
                        } else if (relativeX + left < -widthDiff - gt) {
                            newLeft = -widthDiff - gt;
                        }
                    } else {
                        newLeft = left;
                    }
                    $(image).css({left: newLeft, top: newTop});
                    $.extend(self.imageData, {left: newLeft, top: newTop});
                }
            };
            var dragEnd = function () {
                $D.off(EVENTS.MOUSEMOVE + EVENTS.EVENT_NS, dragMove).off(EVENTS.MOUSEEND + EVENTS.EVENT_NS, dragEnd);
                isDragging = false;
                isMoving = false;
                $('html,body,.magnify-modal,.magnify-stage,.magnify-btn').removeClass('is-grabbing');
            };
            $(stage).on(EVENTS.MOUSESTART + EVENTS.EVENT_NS, dragStart);
        }, draggable: function (modal, dragHandle, dragCancel) {
            var isDragging = false;
            var startX = 0, startY = 0, left = 0, top = 0;
            var dragStart = function (e) {

                e = e || window.event;
                var cancelElem = $(e.target).closest(dragCancel);
                if (cancelElem.length) {
                    return true;
                }
                isDragging = true;  // 0415修改，禁止拖动
                startX = e.clientX;
                startY = e.clientY;
                left = $(modal).offset().left;
                top = $(modal).offset().top;
                $D.on(EVENTS.MOUSEMOVE + EVENTS.EVENT_NS, dragMove).on(EVENTS.MOUSEEND + EVENTS.EVENT_NS, dragEnd);
            };

            var dragMove = function (e) {
                stopPre(e);
                if (isDragging && !isMoving && !isResizing) {
                    var endX = e.clientX;
                    var endY = e.clientY;
                    var relativeX = endX - startX;
                    var relativeY = endY - startY;
                    // $(modal).css({left: relativeX + left, top: relativeY + top});
                    // 0412, BUG: 但图片多了, 需要使用到滚动条时
                    // 这边的top, 是 弹出框到页面最顶部的top值, 所以在移动的时候, top会乱
                    // 解决：最后top的取值直接减去 滚动条$(document).scrollTop()
                    $(modal).css({left: relativeX + left, top: relativeY + top - $(document).scrollTop()})
                }
            };
            var dragEnd = function () {
                $D.off(EVENTS.MOUSEMOVE + EVENTS.EVENT_NS, dragMove).off(EVENTS.MOUSEEND + EVENTS.EVENT_NS, dragEnd);
                isDragging = false;
            };
            $(dragHandle).on(EVENTS.MOUSESTART + EVENTS.EVENT_NS, dragStart);
        }
    };
    $.fn.Magnify = function (options) {
        jqEle = $(this);
        var opts = $.extend(true, {}, defaults, options);
        jqEle.off(EVENTS.CLICK + EVENTS.EVENT_NS).on(EVENTS.CLICK + EVENTS.EVENT_NS, function (e) {
            stopPro(e);
            stopPre(e);
            $(this).data('magnify', new magnify(this, opts));
        });
        return jqEle;
    };

    function stopPro(event) {
        event = event || window.event;
        try {
            event.stopPropagation();
        } catch (e) {
            event.cancelBubble = true;
        }
    }

    function stopPre(event) {
        event = event || window.event;
        try {
            event.preventDefault();
        } catch (e) {
            event.returnValue = false;
        }
    }

    function getImgSrc(ele) {
        return $(ele).data('src') || $(ele).attr('href');
    }

    function preLoadImg(src, success, error) {
        var img = new Image();
        img.onload = function () {
            success(img);
        };
        img.onerror = function () {
            error(img)
        };
        img.src = src;
    }

    function setGrabCursor(imageData, stageData, stage, isRotated) {
        var imgWidth = !isRotated ? imageData.w : imageData.h;
        var imgHeight = !isRotated ? imageData.h : imageData.w;
        if (imgHeight > stageData.h || imgWidth > stageData.w) {
            // stage.addClass('is-grab');
            // 0412: 修改, 移动图片, 遮罩层点击可以close
            // console.log(this);
            // this.$image.addClass('is-grab');
        }
        if (imgHeight <= stageData.h && imgWidth <= stageData.w) {
            stage.removeClass('is-grab')
        }
    }

    function throttle(fn, delay) {
        var timer = null;
        var context = this, args = arguments;
        clearTimeout(timer);
        timer = setTimeout(function () {
            fn.apply(context, args);
        }, delay);
    }
});